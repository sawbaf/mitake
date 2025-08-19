#!/usr/bin/env python3
"""
三竹簡訊 Python 函式庫測試執行器
Mitake SMS Python Library Test Runner

使用方法 / Usage:
    python run_tests.py              # 執行所有測試
    python run_tests.py --verbose    # 執行詳細測試
    python run_tests.py --quick      # 執行快速測試
    python run_tests.py --file test_client  # 執行特定檔案測試
"""

import sys
import os
import unittest
import argparse


def discover_and_run_tests(pattern='test*.py', verbosity=2):
    """發現並執行測試"""
    tests_dir = os.path.join(os.path.dirname(__file__), 'tests')
    
    # 確保可以匯入 tests 資料夾
    if tests_dir not in sys.path:
        sys.path.insert(0, tests_dir)
    
    # 發現測試
    loader = unittest.TestLoader()
    test_suite = loader.discover(tests_dir, pattern=pattern)
    
    # 執行測試
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


def run_quick_tests():
    """執行快速測試（僅核心功能）"""
    print("🚀 執行快速測試...")
    print("=" * 50)
    
    # 執行特定檔案的測試
    patterns = ['test_client.py', 'test_sms.py', 'test_encoding.py']
    
    for pattern in patterns:
        print(f"\n📝 執行 {pattern}...")
        success = discover_and_run_tests(pattern=pattern, verbosity=1)
        if not success:
            print(f"❌ {pattern} 測試失敗")
            return False
    
    print("\n" + "=" * 50)
    print("✅ 快速測試通過！")
    return True


def run_all_tests():
    """執行所有測試"""
    print("🧪 開始執行三竹簡訊 Python 函式庫完整測試套件")
    print("=" * 60)
    
    success = discover_and_run_tests()
    
    print("=" * 60)
    if success:
        print("✅ 所有測試通過！")
    else:
        print("❌ 測試失敗")
    
    return success


def run_specific_test_file(filename):
    """執行特定測試檔案"""
    if not filename.startswith('test_'):
        filename = f'test_{filename}'
    if not filename.endswith('.py'):
        filename = f'{filename}.py'
    
    print(f"📝 執行特定測試檔案：{filename}")
    print("=" * 40)
    
    success = discover_and_run_tests(pattern=filename)
    
    print("=" * 40)
    if success:
        print(f"✅ {filename} 測試通過！")
    else:
        print(f"❌ {filename} 測試失敗")
    
    return success


def run_verbose_tests():
    """執行詳細測試"""
    print("🔍 執行詳細測試...")
    return run_all_tests()


def main():
    """主程式"""
    parser = argparse.ArgumentParser(description='三竹簡訊 Python 函式庫測試執行器')
    parser.add_argument('--verbose', '-v', action='store_true', help='執行詳細測試')
    parser.add_argument('--quick', '-q', action='store_true', help='執行快速測試')
    parser.add_argument('--file', '-f', help='執行特定測試檔案')
    
    args = parser.parse_args()
    
    if args.file:
        success = run_specific_test_file(args.file)
    elif args.quick:
        success = run_quick_tests()
    elif args.verbose:
        success = run_verbose_tests()
    else:
        success = run_all_tests()
    
    # 回傳適當的退出碼
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()