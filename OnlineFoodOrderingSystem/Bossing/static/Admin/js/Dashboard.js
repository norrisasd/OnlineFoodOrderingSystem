var dt = $('#dataTable').DataTable({
    "oLanguage": {
        "sLengthMenu": "Show Entries _MENU_",
    },
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-md-6'l><'col-sm-2'i><'col-md-4'p>>",
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "text-center select-checkbox",
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
    dom: "<'row d-flex flex-row align-items-end'>tr<'row d-flex flex-row align-items-end'<'col-md-6'l><'col-sm-2'i><'col-md-4'p>>",
    "pageLength": 5,
    "order": [],
    "columnDefs": [{
        "targets": 0,
        "orderable": false,
        "className": "text-center select-checkbox",
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