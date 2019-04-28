# 第二届河北省大学生程序设计竞赛
---
## 问题A 2011 Mex Query
时间限制：1s 内存限制:256m
### 描述
Give $n$ non-negative integers, please find the least non-negative integer that doesn’t occur in the $n$ numbers.
### 输入
The first line is an integer $T$, representing the number of test cases. 

For each test case: 

The first line of each test case is an integer $n$.

The second line of each test case are $n$ non-negative integers $a_i$.

$T \leq 10$

$n \leq 2 \times 10^5$

$0 \leq a_i < 2^{31}$
### 输出
or each test case, output a line with the answer.
### 样例输入
```
2
4
4 0 1 3
2
1 1

```
### 样例输入
```
2
0

```
### 提示

---
## 问题B 2012 icebound的商店
时间限制：1s 内存限制:64m
### 描述
icebound在得到神殿的宝藏之后，开了一家神秘的商店。你来到了商店，发现慷慨的icebound搞了$T$次促销活动。在每次促销活动中，icebound都会想出一个他喜欢的数字，如果你买的商品的总价刚好等于icebound喜欢的数字，那么你就可以免费得到这些商品。

icebound的商店里一共有 $15$ 件商品，商品的价格和这家商店一样神秘，第一件商品的价格是 $1$ 元，第二件商品的价格是 $2$ 元，设第$n$件商品的价格为$w_n$元，则：$w_n = w_{n-1} + w_{n-2}  (3 \leq n \leq 15)$。

如果在某次活动中icebound喜欢的数字是 $4$，那么共有 $4$ 种购买方案：

```c++
1. 买 4个 第一种商品
2. 买 2个 第一种商品 和 1个 第二种商品
3. 买 2个 第二种商品
4. 买 1个 第一种商品 和 1个 第三种商品
```

请你算出共有多少种方案可以免费购物，方案数对$1000000009$($=10^9+9$)取模。
### 输入
第一行给出一个整数$T$，表示icebound搞了$T$次活动。

接下来的$T$行每行给出一个正整数$x$，表示在这次活动中icebound喜欢的数字。

$1 \leq T \leq 3000$

$1 \leq x \leq 3000$
### 输出
输出$T$行，每行输出一个正整数。

第$i$行的正整数表示在第$i$次活动中免费购物的方案数，方案数对$1000000009$($=10^9+9$)取模。
### 样例输入
```
3
5
20
30
```
### 样例输入
```
6
134
509
```
### 提示

---
## 问题C 2013 Nim Game
时间限制：1s 内存限制:128m
### 描述
## Description
Nim is a mathematical game of strategy in which two players take turns removing objects from distinct heaps. On each turn, a player must remove at least one object, and may remove any number of objects provided they all come from the same heap _[From Wikipedia, the free encyclopedia]_.  **The goal of the game is to avoid being the player who doesn't have any object to remove. The player who remove the last project is the winner.** 

Now KK and TT are playing Nim game with the optimal strategy. There are $n$ heaps of stones. The number of stones in  $i$ -th heap is $a_i$. They play this game $m$ times, and KK is the player making the first move. During the  $i$ -th time they play the game on the heaps whose index in interval $[l_i,r_i]$. KK wants to know whether he has a winning strategy or not.

### 输入
## Input
The input consists of several test cases. The first line of the input gives the number of test cases, $T(1\le T\le 10^3)$.

For test case, the first line contains two integers $n(1\le n\le 10^6)$ and $m(1\le m\le 10^6)$, representing the number of heap of stones and the game times. 

The second line contains $n$ positive integers $a_1,a_2,\cdots,a_n(1\le a_i\le 10^9)$, representing The number of stones in $i$-th heap.

In the next $m$ lines, each line contains two integers $l_i,r_i$, which means the $$i$$th game is played on the interval $[l_i,r_i]$.

It's guaranteed that $\sum n\le 2\times 10^6$ and $\sum m\le 2\times 10^6$．
### 输出
## Output
For each test case, let $f_i$ represents the answer of the $i$ th game. 

If KK has a winning strategy in the $i$ th game then $f_i=1$, otherwise $f_i=0$.
Please output $\sum f_i*2^{m-i}\ mod\ 10^9+7$，in which $1\le i\le m$．
### 样例输入
```
3
2 1
1 1
1 2
2 1
1 2
1 2
3 2
1 2 2
1 2
2 3

```
### 样例输入
```
0
1
2

```
### 提示

---
## 问题D 2014 Defending Plan Support
时间限制：1s 内存限制:64m
### 描述
The architectural structure of the college is strange, but the rule is that there is only one simple path between every two classrooms. Now the battle between Class A and Class F broke out. As a support staff of Class F, you have to go to every fight in time to help out. With the help of icebound, Class F know the probability of each classroom being attacked. So we define an important degree for each classroom. Now ask you to find a classroom $x$ in $n$ classrooms as your resting base which has the minimum $F(x)$.
$F(x)=\sum w(i) \times d(x,i)$ , $d$ is the distance between $x$ and $i$.
### 输入
The first line is an integer $n$，which is the number of classrooms.

Then $n-1$ lines follow. Each line has three numbers $x, y, z$. There is a road of $z$ meters between $x$ and $y$.

The last line contains $n$ numbers. The $i$-th number $w(i)$ is the important degree of the classroom.

$2 \leq n \leq 5 \times 10^5$,  $0 \leq z,w_i \leq 1000$, $1\leq x,y \leq n$
### 输出
Output a line with an integer, representing the minimum $F(x)$.
### 样例输入
```
5
1 2 1
2 3 1
2 4 1
3 5 6
2 3 1 8 7
```
### 样例输入
```
60
```
### 提示


---
## 问题E 2015 Bitmap
时间限制：2s 内存限制:256m
### 描述
RSYJ is a computer scientist. He has developed many useful image search tools. But now he has encountered some problems.

We use a matrix of $H \times H$ to represent a bitmap with $H \times H$ size, and each pixel of the $8$-bit bitmap is represented by the integer between $[0,255]$.

Now, RSYJ have a $8$-bit bitmap $A$ with $n \times n$ size, and a $8$-bit bitmap $B$ with $m \times m$ size.RSYJ uses an image processing software to copy bitmap $B$ to some  positions in bitmap $A$. Due to RSYJ's computer's error, the value of each pixel in the bitmap $B$ is added with an offset $k$ , which is an integer, but RSYJ doesn't know what $k$ is. 

Now your task is writing a program to help RSYJ find all positions of bitmap $B$ in the bitmap $A$. To simplify the problem, you only need output how many positions of bitmap $B$ in bitmap $A$.

For example, here are two bitmaps $A$ and $B$:

$A$:                   

10  9  3

11  6  5

15  7  2

$B$:

4 3

5 0

Bitmap $B$ was added with an offset: $6$. It becomes:

10  9

11  6

Bitmap $B$ was added with an offset: $2$. It becomes:

6  5

7  2

So there are two positions of bitmap $B$ in bitmap $A$.
### 输入
The first line of the input gives two positive integers $n , m$, representing the size of bitmap $A$ and the size of bitmap $B$, respectively.

The next $n$ lines give the bitmap $A$ . Each line contains $n$ integers.

The next $m$ lines give the bitmap $B$ . Each line contains $m$ integers.

$1 \leq n \leq 2000$,

$1 \leq  m \leq 1000$,

$0 \leq a_{ij} \leq 255$,

$0 \leq b_{ij} \leq 255$

### 输出
Please output an integer, representing the number of positions of bitmap $B$ in bitmap $A$.
### 样例输入
```
3 2
1 2 9
3 4 7
5 6 0
3 4
5 6
```
### 样例输入
```
2
```
### 提示

---
## 问题F 2016 神殿
时间限制：1s 内存限制:128m
### 描述
icebound通过勤工俭学，攒了一小笔钱，于是他决定出国旅游。这天，icebound走进了一个神秘的神殿。神殿由八位守护者守卫，总共由$64$个门组成，每一道门后都有一个迷宫，迷宫的大小均为$100 \times 100$。icebound在迷宫中总共耗时$T$小时，消耗食物$K$公斤。历经千辛万苦之后，icebound终于穿越了迷宫，到达了神殿的中心。神殿的中心有一个宝箱。宝箱上显示有两个正整数$l$和$r$。icebound苦思冥想，终于发现一些打开宝箱的线索。你需要找到一个数$P$，它具有一个美妙的性质：它是$[l,r]$中所有数的二进制表示里，$1$的个数最多的一个数。如果你发现了这个美妙的数字，你就可以打开宝箱，获得巨额财富。

比如$[4,8]$中：

```c++
4: 0100
5: 0101
6: 0110
7: 0111
8: 1000
```

二进制表示中$1$的个数最多的数是$7$，它含有$3$个$1$。
### 输入
输入一行，两个正整数：$l$和$r$，用空格隔开，代表神殿中宝箱上显示的数。

$1 \leq T < 2^{31}$,

$1 \leq K \leq 10^5$, 

$1 \leq l \leq r \leq 2 \times 10^{9}$
### 输出
一个十进制数P，代表满足条件的解。如果有多个P满足条件，输出最小的P。
### 样例输入
```
4 8
```
### 样例输入
```
7
```
### 提示

---
## 问题G 2017 K Multiple Longest Commom Subsequence
时间限制：1s 内存限制:256m
### 描述
KK has two sequences, $A$ and $B$, and wants to find the $k$ multiple longest common subsequence.A sequence $S$ is a $k$ multiple common subsequence of $A$ and $B$ if and only if it satisfies the following conditions:

1) $S$ is a subsequence of $A$ and is a subsequence of $B$. (A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.)

2) The length of $S$ is $t\times k$ where $t$ is a nonnegative integer. The first element of $S$ is $S[1]$. If we divide the sequence into $t$ groups with the $i$th group containing $S[(i - 1) \times k + j] (1 \leq j \leq k)$, for every element $g$, it shares the same value with other elements that are in the same group which $g$ belongs to.

For example, $[1, 1, 2, 2]$ is a double common subsequence of $[1, 2, 3, 1, 2, 3, 2]$ and $[1, 3, 1, 2, 2]$.
KK wants to know the maximum length of such sequence.
### 输入
The first line is an integer $T$, denoting the number of test cases.

For each test case, the first line are three integers $k$ , $n$, $m$, denoting the kind of subsequence, the length of $A$ and the length of $B$.

The second line are $n$ integers $A_1 \sim A_n$, representing the elements of $A$.

The third line are $m$ integers $B_1 \sim B_m$, representing the elements of $B$.

$1 \leq T \leq 10$ , $1\leq k, n, m \leq 10^3$, $1\leq A_i, B_i \leq 10^3$.


### 输出
For each test case, output a line with the maximum length of $k$ multiple common subsequence.

### 样例输入
```
3
1 4 5
1 2 3 4
4 1 3 2 4
2 8 7
1 1 2 2 3 3 4 4
1 2 3 1 2 3 3
3 9 9
1 1 1 2 2 2 3 3 3
1 2 3 1 2 3 1 2 3
```
### 样例输入
```
3
4
3
```
### 提示

---
## 问题H 2018 跑图
时间限制：1s 内存限制:64m
### 描述
跑图是RPG游戏中很烦躁的事情。玩家需要跑到距离他最近的传送点的位置。现在给你一张$N \times M$的方格图，每个方格中数值$0$表示为平地，数值$1$表示为传送点，你的任务是输出一张$N \times M$的矩阵，$Matrix_{xy}$表示从$(x,y)$到距离它最近的传送点的距离。
这里的距离是曼哈顿距离，$(x_1,y_1) \rightarrow(x_2,y_2)$ 的距离为$|x_1-x_2|+|y_1-y_2|$。
### 输入
第一行，有两个数$n,m$。接下来$n$行，每行$m$个数。

数据保证至少有一个传送点。

$1 \leq n \leq 500$，$1 \leq m \leq 500$
### 输出
$n$行，每行$m$个数，表示某个点到离它最近的传送点的距离。
### 样例输入
```
2 3
0 0 0
1 0 1
```
### 样例输入
```
1 2 1
0 1 0
```
### 提示

---
## 问题I 2019 Power Seq
时间限制：2s 内存限制:64m
### 描述
ch给你一个长度为n的数列，有两种操作：

1. ``set l r x`` ：将$[l, r]$内的数全都赋值为$x$。
2. ``query l r`` ：查询$[l, r]$中占主导地位的数字是哪个。

该数字占主导地位，意思是该数在该区间中出现的次数占了区间长度的一半以上（出现一半不算占主导地位）。若没有，则输出$-1$。
### 输入
单组数据。

第一行，一个数：$n$，表示序列长度$(1 \leq n\leq 200000)$。

第二行，$n$个数，分别为$a_1 \sim a_n (0\leq ai\leq 10^6)$。

第三行，一个数$Q$，表示操作的个数$(1 \leq Q\leq200000)$。

接下来的$Q$行，每行一个操作，如题目描述所示，数据保证输入合法。
### 输出
对于每个query操作，输出区间的主导数字是哪个。若不存在，输出$-1$。
### 样例输入
```
10
1 2 1 2 1 2 1 2 1 2
10
query 1 10
query 2 10
query 1 9
set 1 5 3
query 2 3
query 1 10
query 1 9
set 1 10 1
query 2 3
query 1 10

```
### 样例输入
```
-1
2
1
3
-1
3
1
1
```
### 提示

---
## 问题J 2020 Beautiful Array
时间限制：1s 内存限制:256m
### 描述
Senior Pan has two positive integers $x$ and $y$, and she calls an array is a beautiful array if and only if it satisfies the following conditions:

1. The elements in the array are integers.

2. The length of the array is exactly $y$.

3. The product of each element is exactly $x$.

Senior Pan wants you to help her calculate the number of beautiful arrays for different $x$ and $y$.Two arrays $A$ and $B$ are considered different if there exists a position $i$ that $A_i \neq B_i$.

The answer can be very large, so you can just tell her the number mod $10^9+7$.

For example, if $x$ is $2$ and $y$ is $2$, there are four beautiful arrays: $[1, 2]$, $[2, 1]$, $[-1, -2]$, $[-2, - 1]$.
### 输入
The first line is an integer $T$, denoting the number of test cases.

For the following $T$ lines, each line contains two positive integers $x$ and $y$.

$1 \leq T \leq 10^5$,  $x, y \leq 2*10^6$
### 输出
Output $T$ lines, each line contains an integer, representing the number of beautiful array mod $10^9 + 7$.
### 样例输入
```
2
2 2
4 2
```
### 样例输入
```
4
6
```
### 提示

---
## 问题K 2021 520
时间限制：1s 内存限制:512m
### 描述
"又到了五月了呢"，icebound望着五月的天空，眼角流出了泪痕。那一年，icebound还是一个懵懂的少年。那一年，她还是一个青涩纯真的少女。在那一次偶然的相遇之中，他们之间擦出了爱情的火花。他们欢笑着，奔跑着，他们展望着美好的未来，向往着幸福的明天。她像 icebound 心海中的灯塔，像icebound 头顶上的星辰，即使在海里浮沉，即使在夜里摸爬，心中也不会感到迷茫，感到阴寒。他们努力，奋进，向着六月的那一站前行。可是，美好总是短暂的。那海上的灯塔不再发出温情的光亮，那天空中的星辰不再绽放出温柔的色彩。那一站，到达了，icebound 得到了终点，但icebound 永远失去了她，也失去了他的心。

_”侯门一入深似海，从此萧郎是路人“_

今天是2018年5月20日，又是一年的520。这一天，icebound不小心读到上面的诗，icebound沉思着，回想起与她曾经的快乐时光，icebound留下了$n$滴眼泪。icebound的每滴眼泪都带有太多的伤感之情了，以至于每滴眼泪都会感染到其他的生物，使得许多生物都一起掉下了眼泪。kk通过观察得知，当icebound流出$n$滴眼泪时，所有生物产生的眼泪总数为$2^n$。现在，kk需要你帮助他写一个程序，计算当icebound流出$n$滴眼泪时，所有生物产生的眼泪总数$P$，对 $20180520$ 取模。
### 输入
一个正整数$n$，代表icebound留下眼泪的个数。$1 \leq n \leq 2 \times 10^9$
### 输出
一个正整数$P$，代表所有生物产生的眼泪总数，对 $20180520$ 取模。
### 样例输入
```
1
```
### 样例输入
```
2
```
### 提示

---
## 问题L 2022 icebound的账单
时间限制：1s 内存限制:512m
### 描述
icebound从小就有记账的习惯。又到了月末icebound统计资金状况的时候。icebound每个月除了不停的挥霍以外，有时他会良心发现，勤工俭学，因此会有一些微薄的收入。然而icebound数学不好，需要你来帮助他统计他本月的资金状况。

你将会得到一份icebound的账单，一共有 n​ 行整数，其中正数表示icebound打工挣来的收入，负数表示icebound消费的支出。数据保证不会出现 0​ 。

如果icebound本月总收入大于总支出，请你输出“icebound is happy.”；如果本月总收入等于总支出，请你输出“icebound is ok."；如果总收入小于总支出，请你输出"icebound is sad."。
### 输入
第一行，有一个正整数$n$，代表账单有$n$行。

接下来有$n$行，每行一个整数，第$i+1$行整数$a_i$。

$1 \leq n \leq 1000$，$\left| a_i \right|\leq 1000$, $a_i \neq 0$
### 输出
输出一行。如果icebound本月总收入大于总支出，请你输出“icebound is happy.”；如果本月总收入等于总支出，请你输出“icebound is ok."；如果总收入小于总支出，请你输出"icebound is sad."。
### 样例输入
```
2
100
-100
```
### 样例输入
```
icebound is ok.

```
### 提示

