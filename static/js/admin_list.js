var checked_array = []

function checked_array_body()
{
    console.log(checked_array);
}

function handle_bulk_checkbox(self) {
    const table_body = document.getElementById('table_body');
    const set_of_tr = table_body.querySelectorAll('tr');
    set_of_tr.forEach((tr) => {
        var th = tr.querySelector('th:nth-child(1)');
        var checkbox = th.querySelector('input');
        checkbox.checked = self.checked;
        handle_checkbox(checkbox, parseInt(tr.id), false);
    });
}
function handle_checkbox(self, param, checkAll = true) {
    if (!self.checked) {
        remove_from_checked(param);
        const bulk_checkbox = document.getElementById('bulk_checkbox');
        if (bulk_checkbox.checked) {
            bulk_checkbox.checked = false;
        }
    } else {
        add_to_checked(param);
        if (checkAll) {
            check_all_unit_checkboxes();
        }
    }
}

function check_all_unit_checkboxes() {
    const table_body = document.getElementById('table_body');
    const set_of_tr = table_body.querySelectorAll('tr');
    const allChecked = Array.from(set_of_tr).every((tr) => {
        const checkbox = tr.querySelector('th:nth-child(1) input');
        return checkbox.checked;
    });
    document.getElementById('bulk_checkbox').checked = allChecked;
}

function add_to_checked(param)
{
    if(!checked_array.includes(param))
        {
            checked_array.push(param);
        }
}

function remove_from_checked(param)
{
    checked_array = checked_array.filter(item => item !== param);
}

function delete_checked_products(e){
    if(checked_array.length === 0 ) return;
    if(!confirm('Are you sure?')){
        // console.log("Cancel");
        e.preventDefault();
    }else{
        delete_model_instances();
        bulk_checkbox = document.getElementById('bulk_checkbox');
        if(bulk_checkbox.checked){
            bulk_checkbox.checked = false;
        }
    }
}

function delete_model_instances()
{
    fetch('/delete_models/',{
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            'ids': checked_array
        })
    }).then(response => response.json())
    .then(data=> {
        if (data.status === 'success'){
            console.log('Model instances deleted successfully');
            updateUI(checked_array);
            checked_array = [];
        } else {
            console.error('Error deleting model instances:', data.message);
        }
    }).catch(error => {
        console.error('Error:', error)
    });
}

function updateUI(deletedIds){
    deletedIds.forEach(id => {
        const element = document.getElementById(id);
        if(element){
            element.remove();
        }
    });
}

function getCookie(name){
    let cookieValue = null;
    if(document.cookie && document.cookie !== ''){
        const cookies = document.cookie.split(';');
        for(let i=0 ; i < cookies.length; i++){
            const cookie = cookies[i].trim();
            if(cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}