

function updateTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();
    var timeString = hours + ':' + (minutes < 10 ? '0' : '') + minutes + ':' + (seconds < 10 ? '0' : '') + seconds;
    document.getElementById('current-time').innerText = 'Hora: ' + timeString;
}

setInterval(updateTime, 1000);

$(document).ready(function () {
    $('#myTabs a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
    });
});
