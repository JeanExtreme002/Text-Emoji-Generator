# Text Emoji Generator:

Are you tired of wasting time copying and pasting text emojis in chats with friends? So why don't you use this application? 
With this program, you can easily generate emojis in your chat without having to stop typing in the chat to search for an emoji.

# Dependencies:

Type the command below on the terminal to install all dependencies:
```
$ pip install -r requirements.txt
```

# Setting:

To configure the shortcut keys, open the `settings.json` file and change the keys in the` master_key` option. <br>

You can also choose to generate the emoji directly in the chat or copy the emoji to the clipboard by setting 
the `clipboard` option to **true**.

```
{
    "clipboard": false,
    "master_key": [
        "insert"
    ]
}
```

# Adding emojis:

To change or add new emojis, open the file `keys_and_emojis.json` and configure a key for each emoji.

```
{
    "z": "( ͡° ͜ʖ ͡°)",
    "x": "¯\\_(ツ)_/¯",
    "c": "(^o^)丿",
    "v": "(づ｡◕‿‿◕｡)づ",
    "b": "(づ￣ ³￣)づ",
    "n": "(ㆆ_ㆆ)",
    "m": "（っ＾▿＾）"
}
```
