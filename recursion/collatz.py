def collatz(n):
    # エラーチェック
    if n <= 0:
        raise Exception("positive integers are required")


    print('#'*int(n/10)+f" {n}")
    # 処理
    if n == 1:
        print('\n'*2+'_'*10+' '*3+"1になりました"+'\n'*2)
        return
    else:
        if n%2 == 0:
            collatz(n/2)
        elif n%2 == 1:
            collatz(3*n+1)

# テストコード
# collatz(1)
# collatz(3)
print('\n'*2+'_'*10+' '*3+"コラッツ予想 : 185の場合"+'_'*10+'\n')
collatz(185)
# collatz(973947)
# collatz(0)
# collatz(-1)