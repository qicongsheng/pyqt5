// 初始化pyjs对象
document.addEventListener("DOMContentLoaded", function () {
    new QWebChannel( qt.webChannelTransport, function(channel) {
        window.pyjs = channel.objects.JsBridge;
    });
});
