<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>百度百科——全球领先的中文百科全书</title>
    <style>
    p {
        margin: 0;
    }
    .baikeLogo {
        width: 780px;
        height: 50px;
        margin: 150px auto 75px;
        text-indent: -9999em;
        background: url(https://img.baidu.com/img/baike/logo-baike.png) 50% 50% no-repeat;
    }
    /* S-- errorBox */
        .errorBox {
            width: 780px;
            margin: 0 auto 65px;
            text-align: center;
            font-family: "Microsoft yahei";
        }
        .errorBox .timeOut {
            color: #666;
            font-size: 16px;
        }
        .errorBox .timeOut a {
            color: #136ec2;
            text-decoration:none;
        }
        .errorBox .countdown {
            font-weight: 700;
        }
    /* E-- errorBox */

    /* S-- sorryBox */
        .sorryBox {
            position: relative;
            margin-bottom: 10px;
        }
        .sorryBox .sorryTxt {
            color: #559ee7;
        }
        .sorryBox .sorryCont {
            color: #333;
            font-size: 35px;
        }
        .sorryBox .sorryBubble {
            position: absolute;
            left: 98px;
            top: -35px;
            width: 72px;
            height: 37px;
            background: url(/static/common/img/error_bubble_7da2966.jpg) no-repeat 50% 50%;
        }
    /* E-- sorryBox */

    /* S-- footer */
        .ft {
            width: 780px;
            margin: 0 auto 65px;
            padding-top: 20px;
            padding-bottom: 20px;
            line-height: 20px;
            color: #666;
            font-size: 12px;
            text-align: center;
            background-color: #f8f8f8;
        }
        .ft a{
            color: #2d64b3;
            text-decoration: none;
        }
        .ft a:hover {
            text-decoration: underline;
        }
        .feedBackWays .ul {
            margin: 0;
            padding: 0;
        }
        .feedBackWays .li {
            list-style: none;
        }
        .ftCont {
            margin-top: 20px;
            color: #2d64b3;
        }
    /* E-- footer */
    </style>
</head>
<body>
    <div id="bd">
        <h1 class="baikeLogo">
            百度百科错误页
        </h1>
        <div class="errorBox">
            <!-- 主体 -->
            <div class="sorryBox">
                <div class="sorryBubble"></div>
                <p class="sorryCont"><span class="sorryTxt">抱歉</span>，您所访问的页面不存在...</p>
            </div>
            <div class="timeOut">
                <p><span class="countdown" id="countdown">3</span>秒后自动跳转到<a href="http://baike.baidu.com/">百科首页</a></p>
            </div>
            <!-- /主体 -->
        </div>
    </div>
    <div id="ft">
        <div class="ft">
            <div class="feedBackWays">
                <ul class="ul">
                    <li class="li">如果想提出功能问题或意见建议,请到<a href="http://baike.baidu.com/feedback" target="_blank">意见反馈</a>;</li>
                    <li class="li">如果您要举报侵权或违法信息,请到<a href="http://help.baidu.com/newadd?prod_id=10&category=1" target="_blank">投诉中心</a>;</li>
                    <li class="li">其他问题请访问<a href="http://tieba.baidu.com/f?kw=%B0%D9%B6%C8%B0%D9%BF%C6" target="_blank">百度百科吧</a>。</li>
                </ul>
            </div>
            <div class="ftCont">
                &copy;<span id="copyYear"></span>Baidu <a href="http://www.baidu.com/duty/" target="_blank">使用百度前必读</a> | <a href="http://help.baidu.com/question?prod_en=baike&class=89&id=1637" target="_blank">百科协议</a> | <a href="http://baike.baidu.com/hezuo/" target="_blank">百度百科合作平台</a>
            </div>
        </div>
    </div>
    <script type="text/javascript">
    window.onload = function(){
        var time = 3,
            year = new Date().getFullYear();

        document.getElementById("copyYear").innerHTML = year;
        setInterval(function(){
            if (time == 0){
                window.location = "http://baike.baidu.com/";
                return;
            }
            document.getElementById("countdown").innerHTML = time;
            time--;
        }, 1000);
    }
    </script>
</body>
</html>