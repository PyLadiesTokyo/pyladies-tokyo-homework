# 問題002: 奇数を表示しよう

 100までの自然数の中に存在する奇数を表示してください。

```
# 表示例
1
3
5
7
（略）
97
99
```

表示方法は自由です。
上の数値が表示されたら正解です。
対象が1000まで、1万までになっても同じように動作するように実装します。

## ヒント
- 奇数とは2で割り切れない数値です。
- x%2 で2で割った余りが求められます。
- range(x, y, step) を利用する方法もあります