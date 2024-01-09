javascript:(
    function(s){
        let hour_start = 16;
        let hour_num = 2; 
        const rows = document.getElementById('ContentPlaceHolder1_Step2_data').getElementsByTagName("table")[0].getElementsByTagName("tr");
        const place_num = 14; const base_idx = rows.length - ((18 - hour_start) * place_num);
        let found = false;

        for (let i = 0; i <= 7; i += 1){
            all_available = true;
            for (let j = 0; j < hour_num; j += 1){ 
                idx = base_idx + i + (j * place_num);
                if (rows[idx].lastElementChild.firstElementChild.title == '已被預約') {
                    all_available = false;
                    break;
                }
            }

            if (all_available){
                for (let j = 0; j < hour_num; j += 1){
                    idx = base_idx + i + (j * place_num);
                    rows[idx].lastElementChild.bgColor = "#FF8888";
                }
                
                found = true;
            }
        }

        if (found == false){
            alert('無符合條件場地');
        }
    }
)();