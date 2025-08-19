# 三竹簡訊 Python 函式庫 Makefile

.PHONY: test test-quick test-verbose install clean help

# 預設目標
all: test

# 執行所有測試
test:
	@echo "🧪 執行所有測試..."
	@python run_tests.py

# 執行快速測試
test-quick:
	@echo "🚀 執行快速測試..."
	@python run_tests.py --quick

# 執行詳細測試
test-verbose:
	@echo "🔍 執行詳細測試..."
	@python run_tests.py --verbose

# 安裝依賴
install:
	@echo "📦 安裝相關套件..."
	@pip install -e .

# 清理臨時檔案
clean:
	@echo "🧹 清理臨時檔案..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

# 檢查編碼問題
test-encoding:
	@echo "🌏 測試中文編碼..."
	@python -c "from mitake import MitakeClient; print('測試訊息：你好，我是小海！'); print('UTF-8 編碼測試通過 ✅')"

# 測試特定檔案
test-client:
	@echo "🔧 測試客戶端功能..."
	@python run_tests.py --file test_client

test-sms:
	@echo "📱 測試簡訊功能..."
	@python run_tests.py --file test_sms

test-encoding-file:
	@echo "🌏 測試編碼功能..."
	@python run_tests.py --file test_encoding

# 顯示幫助
help:
	@echo "三竹簡訊 Python 函式庫 Makefile"
	@echo ""
	@echo "可用指令："
	@echo "  make test           - 執行所有測試"
	@echo "  make test-quick     - 執行快速測試"
	@echo "  make test-verbose   - 執行詳細測試"
	@echo "  make test-client    - 測試客戶端功能"
	@echo "  make test-sms       - 測試簡訊功能"
	@echo "  make test-encoding-file - 測試編碼功能"
	@echo "  make install        - 安裝函式庫"
	@echo "  make clean          - 清理臨時檔案"
	@echo "  make test-encoding  - 測試中文編碼"
	@echo "  make help           - 顯示此幫助訊息"