# 注意

ruby-numo/narray
ruby-numo/linalg

をつかうとき，

```
gem install narray
```

したnarrayではlinalgのインストールができない（narray.h not foundとなる）．

そのため，ここではnarrayとlinalgの両方を手元でビルドすることにしている（綺麗にbundle installする方法があったら教えて下さい）．

```
git clone git@github.com:ruby-numo/narray.git
git clone git@github.com:ruby-numo/linalg.git
cd narray; rake build; gem install pkg/numo-narray-*.gem
cd ../linalg; rake build; gem install pkg/numo-linalg-*.gem -- --with-blas
```



### openblas

numo-linalgはLAPACKもしくはOpenBLASが必要です．

私は/optにビルドしています．

```
git clone git@github.com:xianyi/OpenBLAS.git
cd OpenBLAS; make PREFIX=/opt/OpenBlas; make PREFIX=/opt install
```


# つかっている外部ライブラリ

Gemfileで管理したい...（numo関係が解決したら...）

```
gem install 'stopwords'
```
