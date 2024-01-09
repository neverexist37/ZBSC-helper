javascript:(
    function(s){
        let hour_start = 16;
        let hour_num = 2; 
        const rows = document.getElementById('ContentPlaceHolder1_Step2_data').getElementsByTagName("table")[0].getElementsByTagName("tr");
        const place_num = 14;
        const base_idx = rows.length - ((18 - hour_start) * place_num);
        const place_id_list = [83, 84, 1074, 1075, 87, 88, 2115, 2116];
        const query_date = document.getElementById('ContentPlaceHolder1_Date_Step2_lab').firstElementChild.value;
        let found = false;

        for (let i = 0; i <= 7; i += 1){
            all_available = true;
            for (let j = 0; j < hour_num; j += 1){
                idx = base_idx + i + (j * place_num);
                if (rows[idx].lastElementChild.firstElementChild.title == '已被預約'){
                    all_available = false;
                    break;
                }
            }

            if (all_available){
                let place_id = place_id_list[i];
                for (let j = 0; j < hour_num; j += 1){
                    let query_hour = hour_start + j;
                    url = '../fe02.aspx?module=net_booking&files=booking_place&StepFlag=25&PT=1';
                    url += '&QPid=' + place_id + '&QTime=' + query_hour + '&D=' + query_date;
                    window.open(url, '_blank');
                }
                
                found = true;
                break;
            }
        }
        
        if (found == false){
            alert('無符合條件場地');
        }
    }
)();