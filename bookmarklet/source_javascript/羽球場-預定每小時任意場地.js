javascript:(
    function(s){
        const rows = document.getElementById('ContentPlaceHolder1_Step2_data').getElementsByTagName("table")[0].getElementsByTagName("tr");
        const place_num = 14;
        const place_id_list = [83, 84, 1074, 1075, 87, 88, 2115, 2116];
        const query_date = document.getElementById('ContentPlaceHolder1_Date_Step2_lab').firstElementChild.value;
        let found = false;
        let start_row_idx = rows.length - place_num;
        
        while (start_row_idx > 0){
            for (let i = 0; i <= 7; i += 1){
                idx = start_row_idx + i;
                if (rows[idx].lastElementChild.firstElementChild.title != '已被預約'){
                    let place_id = place_id_list[i];
                    let query_hour = rows[start_row_idx].firstElementChild.innerText.substring(0, 2);
                    url = '../fe02.aspx?module=net_booking&files=booking_place&StepFlag=25&PT=1';
                    url += '&QPid=' + place_id + '&QTime=' + query_hour + '&D=' + query_date;
                    window.open(url, '_blank');
                    found = true;
                    break;
                }
            }
            
            start_row_idx -= place_num;
        }

        if (found == false){
            alert('無符合條件場地');
        }
    }
)();