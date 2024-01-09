javascript:(
    function(s){
        let date = new Date();
        date.setDate(date.getDate() + 7);
        date_str = date.toLocaleDateString('zh-TW');
        let url = 'https://fe.xuanen.com.tw/fe02.aspx?module=net_booking&files=booking_place&StepFlag=2&PT=1';
        url += '&D2=2&D=' + date.toLocaleDateString('zh-TW');
        url += '#ContentPlaceHolder1_Panel_Step2';
        window.open(url, '_blank');
    }
)();