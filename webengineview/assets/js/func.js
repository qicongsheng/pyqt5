function pyCallJqueryFunc(divId, msg) {
    $('#' + divId).val(msg)
}
function jsCallPy() {
    alert(3)
    pyjs.js_call_py('我是js传给python的值', function(result) {
        alert("JS Alert:" + result);
    });
}
function pyCalljs(msg) {
    alert("JS Alert: py调用js：" + msg);
    return 'js收到：' + msg
}