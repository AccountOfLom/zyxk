// ==UserScript==
// @name         网站浏览统计
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  网站浏览统计
// @author       You
// @match        http*://*/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function webSiteHistory()
    {
        //人员ID
        var mid = 6;
        //电脑ID
        var cid = 1;

        //当前域名
        var domain = window.location.hostname;
        //网页顶部栏标题
        var title = document.title;

        // 原生 ajax 请求
        var xhr = new XMLHttpRequest();
        //url传参
        var urlParams = "mid=" + mid +"&cid=" + cid +"&domain=" + domain + "&title=" + title;
        xhr.open("GET", "http://127.0.0.1:5000/history?" + urlParams, true);

        // 设置请求头，通知服务器内容类型为application/x-www-form-urlencoded
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                // 请求成功
                console.log(xhr.responseText);
            }
        };

        // 发送请求
        xhr.send();
    }

    setInterval(function() {
        webSiteHistory()
    }, 4000); // 放宽1秒偏移量

})();