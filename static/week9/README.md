## Question
1. 以下三个div将会会如何放置(margin collapsing)？
    ``` html
    <style>
    body {
        margin: 0;
    }

    .first {
        margin: 20px;
        height: 500px;
        background-color: #666;
    }

    .second {
        margin: -10px;
        height: 300px;
        background-color: #999;
    }

    .third {
        margin: -30px;
        height: 100px;
        background-color: #ccc;
    }
    </style>
    <div class="first">
        <div class="second">
            <div class="third">
                三个元素的外边距折叠
            </div>
        </div>
    </div>
    ``` 
1. 同一个BFC中，相邻的块状元素都是垂直放置吗？
2. 如何清除浮动？根据什么原理？
3. 如何对左侧栏200px，主内容自适应进行布局？
4. 如何使用margin完成圣杯布局（左侧x px，右侧y px，中间自适应），用flex呢？

## Answer
1. 以下三个div将会会如何放置？

    在同一个BFC中，相邻的块状
    元素会发生折叠。两个margin值都是正值，取最大值，都是负值，取最小值，一正一负则相加。那么如题有三个呢，是从父元素往子元素算起，还是子元素往外算起？如果从外往里算，是0，从内往外算是-10px。经测试，是从内往外计算。

    [多边距折叠 demo](http://shfshanyue.applinzi.com/week9/margin-compute.html)
1. 同一个BFC中，相邻的块状元素都是垂直放置吗？

    不一定，设置`writing-mode`值。查看以下Demo。

    [水平折叠的外边距 demo](http://shfshanyue.applinzi.com/week9/margin-horizontal.html)
2. 如何清除浮动？根据什么原理？
    + 紧挨的块级元素设置`clear both`来清除浮动，一般 会通过`:after`清除浮动。如Bootstrap的`clearfix`。
        ``` css
        .clearfix {
            display: table;
            content: " ";
            clear: both
        }
        ```
    + 使父级元素触发一个新的BFC，如`overfow:hidden`或者`display:table`。

    [清除浮动 demo](http://shfshanyue.applinzi.com/week9/clear.html)
3. 如何对左侧栏200px，主内容自适应进行布局？ 

    左栏设置200px的宽，设置浮动，主内容设置`overflow:hidden`触发一个BFC。因为BFC不会与浮动折叠，所以右侧会自适应。

    [左固定右自适应布局 demo](http://shfshanyue.applinzi.com/week9/two-column.html)
4. 如何使用margin完成圣杯布局（左侧x px，右侧y px，中间自适应），用flex呢？

    圣杯布局大致结构如下
    ``` html
    <div class="header"></div>
    <div class="container">
        <div class="main"></div>
        <div class="left"></div>
        <div class="right"></div>
    </div>
    <div class="footer"></div>
    ```
    步骤如下：
    1. .container设置内边距，留出放置左右固定宽度侧栏的宽度。设置`min-width:x px`（content-box）下，如果.left宽度大于父元素content-box的宽度，自己会被挤下去。
    1. .main，.left，.right设置浮动，.main设置100%的宽度。.main位置固定。
    1. .left设置x px宽度，设置margin-left为-100%，此时与.main左上角重合，设置`position:relative`，left设为-x px或者right设置x px，.left位置固定。
    1. .right设置y px宽度，把margin-left设为-y px，此时与.main右上角重合，相对定位回到自己的位置。(或者margin-right小于等于-y px，最后不用定位，查看[margin demo2](http://shfshanyue.applinzi.com/week9/shengbei2.html))。
    1. footer设置`clear:both`清除浮动，或者container设置为`display:table`或者`overflow:hidden`闭合浮动。使.footer回到正常位置。

    另外有flex布局就简单多了。需要注意的是使用margin会把.main放在最前边。而flex可以按照.left，.main，.right的顺序放置。另外flex布局也不会出现中间挤掉两边的情况。

    [圣杯布局 demo1](http://shfshanyue.applinzi.com/week9/shengbei1.html)

    [圣杯布局 demo2](http://shfshanyue.applinzi.com/week9/shengbei2.html)

    [flex完成圣杯布局 demo](http://shfshanyue.applinzi.com/week9/flex.html)
