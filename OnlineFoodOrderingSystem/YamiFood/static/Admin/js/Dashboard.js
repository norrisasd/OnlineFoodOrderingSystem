var dt = $('#dataTable').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "text-center select-checkbox",
    },{
        "targets": 5,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
});

var dt1 = $('#dataTable1').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "select-checkbox",
    },{
        "targets": 5,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
});

var dt2 = $('#dataTable2').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "select-checkbox",
    },{
        "targets": 5,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
});

var dt3 = $('#dataTable3').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-auto'l><'col-md-8'i><'col-md-2'p>>",
    "lengthMenu": [5,10, 25, 50,],
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "select-checkbox",
    },{
        "targets": 3,
        "orderable": false,
        "className": "text-center",
        width: 100,
    }],
    select: {
        style: 'multi',
        selector: 'tr>td:nth-child(1)'
    },
    "paging": true,
    "searching": true,
    "ordering": true,
    "info": true,
    "autoWidth": false,
    "responsive": true,
});

// new $.fn.dataTable.Buttons(dt, {
//     "buttons": [{
//         extend: 'excel',
//         text: 'Excel Selected',
//         exportOptions: {
//             modifier: {
//                 selected: true
//             }
//         },
//     }, {
//         extend: 'pdf',
//         text: 'PDF Selected',
//         exportOptions: {
//             modifier: {
//                 selected: true
//             }
//         },
//     }, {
//         extend: 'print',
//         text: 'Print Selected',
//         exportOptions: {
//             modifier: {
//                 selected: true
//             }
//         },
//     }]
// }).container().appendTo('#beforeLD1');
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function hideAll(){
    w3.hide('#UserTable');
    w3.hide('#ProductTable');
    w3.hide('#OrderTable');
    w3.hide('#DeliveryTable');
}
function addProduct(data) {
    $.ajax({
        type: 'post',
        url: '',
        data: new FormData(data),
        contentType: false,
        cache: false,
        processData: false,
        success: function (response) {
            if (response.status) {
                toastr.success("Product Added");
                $(".modal").modal("hide");
                refreshTable();
                $('#ProductForm').trigger("reset");
            }else{
                toastr.error(response.status);
            }
        }
    });
    return false;
}
function addEmployee(data){
    $.ajax({
        type: 'post',
        url: '',
        data: new FormData(data),
        contentType: false,
        cache: false,
        processData: false,
        success: function (response) {
            if (response.status) {
                toastr.success("Employee Added");
                $(".modal").modal("hide");
                refreshTable();
                $('#EmployeeForm').trigger("reset");
            }else{
                toastr.error(response.status);
            }
        }
    });
    return false;
}

function updateUser(form){
    if (confirm("Are you sure you want to save changes?")){
        $.ajax({
            type: 'post',
            url: '',
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data: new FormData(form),
            contentType: false,
            cache: false,
            processData: false,
            success: function (response) {
                if (response.status) {
                    toastr.success("User Updated");
                    $(".modal").modal("hide");
                    refreshTable();
                    $('#UserForm').trigger("reset");
                    refreshTableUser();
                }else{
                    toastr.error(response.status);
                }
            }
        });
    }
    
    return false;
}
function addToCart(id){
    $.ajax({
        type:'post',
        url:'',
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        data:{
            request:"addToCart",
            product_id:id,
        },
        success:function(response){
            if(response.check){
                openNav();
                refreshCart();
            }
        }
    });
}
function refreshTable() {
    let cb = '';
    $.ajax({
        type: 'get',
        url:'',
        data:{
            request:"getProducts"
        },
        success: function (response) {
            data = JSON.parse(response.products);
            dt1.clear().draw();
            for (var da in data){
                dt1.row.add([
                    cb,
                    data[da].pk,
                    data[da].fields.product_name,
                    data[da].fields.product_category,
                    data[da].fields.price,
                    `<a class="btn btn-outline-secondary text-center"
                    style="padding-left:15px;padding-right: 15px;" href="#"><i
                        class="fas fa-eye"></i></a>`
                ]).draw();
            }
            
            
            
        }
    });
    return false;
}
function deleteProduct(id){
    if(confirm("Are you sure you want to delete this product")){
        $.ajax({
            type:'post',
            url:'',
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data:{
                request:"deleteProduct",
                product_id:id
            },
            success:function(response){
               if(response.status){
                   toastr.success("Product Deleted");
                   $(".modal").modal("hide");
                    refreshTable();
                    $('#ProductForm').trigger("reset");

               }
            }
        });
    }
    return false;
}
function deleteUser(id){
    if(confirm("Are you sure you want to delete this user")){
        $.ajax({
            type:'post',
            url:'',
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data:{
                request:"deleteUser",
                user_id:id
            },
            success:function(response){
               if(response.status){
                   toastr.success("User Deleted");
                   $(".modal").modal("hide");
                    refreshTableUser();
                    $('#UserForm').trigger("reset");

               }
            }
        });
    }
    return false;
}
function deleteOrder(form){
    $.ajax({
        type: 'post',
        url: '',
        data: new FormData(form),
        contentType: false,
        cache: false,
        processData: false,
        success: function (response) {
            if (response.status) {
                toastr.success("Order Deleted");
                $(".modal").modal("hide");
            }else{
                toastr.error(response.status);
            }
        }
    });
    return false;

}
function updateProduct(form){
    if(confirm("Are you sure you want to save changes?")){
        $.ajax({
            type: 'post',
            url: '',
            data: new FormData(form),
            contentType: false,
            cache: false,
            processData: false,
            success: function (response) {
                if (response.status) {
                    toastr.success("Product Updated");
                    $(".modal").modal("hide");
                    refreshTable();
                    $('#ProductForm').trigger("reset");
                }else{
                    toastr.error(response.status);
                }
            }
        });
       
    }
    return false;
}
function updateUserForm(id){
    $('#userView-'+id+' #UserForm')
}
function refreshTableUser() {
    let cb = '';
    $.ajax({
        type: 'get',
        url:'',
        data:{
            request:'getUsers'
        },
        success: function (response) {
            data = JSON.parse(response.products);
            dt.clear().draw();
            for (var da in data){
                dt.row.add([
                    cb,
                    data[da].pk,
                    data[da].fields.first_name,
                    data[da].fields.last_name,
                    data[da].fields.is_admin == 1 ? 'Employee' : 'Customer',
                    `<button type="button" class="btn btn-outline-secondary text-center" data-toggle="modal" data-target="#userView-`+data[da].pk+`"
                    style="padding-left:15px;padding-right: 15px;"> <i class="fas fa-eye"></i>
                </button>`
                ]).draw();
            }
            
            
            
        }
    });
    return false;
}
function refreshCart(){
    let body='';
    let prodName='';
    $.ajax({
        type: 'get',
        url:'',
        data:{
            request:"getMyCart"
        },
        success: function (response) {
            data = JSON.parse(response.cart);
            prod = JSON.parse(response.products);
            for(var da in data){
                for(var p in prod){
                    if(prod[p].pk == data[da].fields.product_id)
                        prodName=prod[p].fields.product_name;
                }
                body +=`
                <li>
                    <div class="row">
                        <div class="col">
                            <span>`+prodName+`</span>
                        </div>
                        <div class="col-auto">
                            <input type="number" class="form-control" min="0" max="50" value="`+data[da].fields.quantity+`"/>
                        </div>
                        <div class="col-auto"><a href="javascript:void(0)" class="text-secondary"
                                style="padding:0;" onclick='removeItem("`+data[da].pk+`")'><span>&times;</span></a></div>
                    </div>
                </li>
                `;
            }
            $('#cartlist').html(body);
            
            
        }
    });
}
function checkPassword(value){
    pass = $("#password").val();
    if(pass == value){
        document.getElementById("btnAddEmployee").disabled = false;
    }else{
        document.getElementById("btnAddEmployee").disabled = true;
    }
}
/* Set the width of the side navigation to 250px and the left margin of the page content to 250px and add a black background color to body */
function openNav() {
    document.getElementById("mySidenav").style.width = "400px";
    w3.show("#mycart");
    // document.getElementById("main").style.marginLeft = "250px";
    // document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }
  
  /* Set the width of the side navigation to 0 and the left margin of the page content to 0, and the background color of body to white */
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    w3.hide("#mycart");
    // document.getElementById("main").style.marginLeft = "0";
    // document.body.style.backgroundColor = "white";
  }
  function removeItem(index){
      $("#cartlist li:nth-child("+index+")").remove();    
  }