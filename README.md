# python-opt

python による数理最適化入門

## 2.1 線形最適化問題入門

    毎日，オレンジ60kg, りんご36kg，ぶどう48kg を仕入れる
    ミックスジュースA, B, Cを製造・販売している
    A 1L: オレンジ3kg, りんご1kg           : 150 yen
    B 1L: オレンジ1kg, りんご3kg, ぶどう2kg : 200 yen
    C 1L: オレンジ2kg,           ぶどう4kg : 300 yen
    利益最大化するA, B, Cの生産量は?

A, B, Cの生産量をそれぞれ $`a`$L，$`b`$L，$`c`$L とすると，売上は
$$150a+200b+300c$$
で，これを最大化したい．
マイナスの生産量は認めないので $a>0, b>0, c>0.$
各素材の仕入れ量が制限されているので

$$
3a+b+2c<60
$$

$$
a+3b<36
$$

$$
2b+4c<48
$$

コード [2-1.py](2-1.py)
