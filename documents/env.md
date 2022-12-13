#　環境構築
- https://www.currypurin.com/entry/2022/12/03/160204
- https://zenn.dev/algovitae/articles/2022devcontainer
- Ubuntu22ではiptablesの設定を変える必要がある？
- build で失敗したコマンドをpowershellで実行するとうまくいった

# スニペット
- https://zenn.dev/algovitae/articles/2022devcontainer

# コマンド
```
acc new abc279
acc submit main.py
oj t -c " python3 ./main.py" -d ./tests/
```

#  ファイル上にインプットテキスト
```python
import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)
```

