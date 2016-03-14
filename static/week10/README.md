# 2016-03-07 - 2016-03-13
## python
+ 使用闭包完成Add函数的编写

    ``` python
    c1 = add(10)
    c2 = add(20)

    print c1(), c2(), c1(), c2()

    out: 11 21 12 22
    ```
    python2的话，闭包中无法修改外部变量，可以使用可变对象如list代替，在python3中可以使用`nonlocal`关键字。写Class也能使用 __\__call\____ 方法完成，不过只有一个方法，没必要使用类。
    ``` python
    # python3
    def add(n):
        def inc():
            nonlocal n
            n += 1
            return n
        return inc

    # python2
    def add(n):
        t = [n]
        def inc():
            t[0] += 1
            return t[0]
        return inc

    # class
    class Add(object):
        def __init__(self, n):
            self.n = n

        def __call__(self):
            self.n += 1
            return self.n
    ```


## FE
+ 以sticky定位以及老方法实现一个导航粘性布局的效果

    position:sticky可以很简单的实现这个功能，以前的实现方法是监听`scroll`事件，根据元素`offsetY`与`window.scrollY`比较进行fixed定位的切换。

    [sticky效果图](http://shfshanyue.applinzi.com/week10/sticky.html)

    [fixed效果图](http://shfshanyue.applinzi.com/week10/week10/relative-and-fixed.html)
+ __实现可发送 JSONP 请求、获取 JSONP 返回结果的函数__

    ```
    JSONP(url, {
        data: {
            key1: value1
        },
        callback: function (data) {
            // data 是服务端返回的数据
        }
    })
    ```
    
    使用flask做服务器，模拟数据，根据url参数callback做出相应的相应。

    [代码地址](https://github.com/shfshanyue/review-weekly/tree/master/static/week10/jsonp)
    
## util
+ fiddler如何配置使得监听https
    
    fiddler通过设置代理，使得所有http请求需要通过fiddler，来达到监听traffic的作用。而https将数据交给TLS/SSL层进行加密，再进行TCP传输，能够有效避免他人在中间结点劫持流量。于是此时通过fiddler监听https请求数据，浏览器会提示不安全的链接。可以在fiddler上设置安全证书解决。在菜单栏中__Tools -> Fiddler Options -> HTTPS__勾选`Capture HTTPS CONNECTs`与`Decrypt HTTPS trafic`。如果未生效，重置所有证书生效。
+ ~~fiddler监听移动端贴吧的http请求，模拟贴吧的自动签到~~

    fiddler监听移动端流量，保证PC与移动端在相同的无线网络下，移动端连接无线时设置代理服务器与端口号和fiddler一致。