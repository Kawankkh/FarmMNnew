$("#delList").click(function(e) {
    e.preventDefault();
    var btn = "button";
    Swal.fire({
        title: 'ต้องการจะลบข้อมูล?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'ลบข้อมูล',
        cancelButtonText: 'ยกเลิก'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({
            icon: 'success',
            title: 'ลบข้อมูสำเร็จ!',
            showConfirmButton: false,
            timer: 1500
          }
          )
        }
      });
  });
  


  $("#delfarmerlist").click(function(e) {
    e.preventDefault();
    var btn = "button";
    Swal.fire({
        title: 'ต้องการจะลบข้อมูล?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'ลบข้อมูล',
        cancelButtonText: 'ยกเลิก'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({
            icon: 'success',
            title: 'ลบข้อมูสำเร็จ!',
            showConfirmButton: false,
            timer: 1500
          }
          )
        }
      });
  });



  $("#saveFarmerlist").click(function(e) {
    e.preventDefault();
    var btn = "button";
    Swal.fire({
        title: 'คุณต้องการที่จะข้อมูล?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'บันทึกข้อมูล',
        cancelButtonText: 'ยกเลิก'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({
            icon: 'success',
            title: 'บันทึกข้อมูลสำเร็จ!',
            showConfirmButton: false,
            timer: 1500
          }
          )
        }
      });
  });

  $("#savefarmerItem").click(function(e) {
    e.preventDefault();
    var btn = "button";
    Swal.fire({
        title: 'คุณต้องการที่จะข้อมูล?',
        icon: 'info',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'บันทึกข้อมูล',
        cancelButtonText: 'ยกเลิก'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire({
            icon: 'success',
            title: 'บันทึกข้อมูลสำเร็จ!',
            showConfirmButton: false,
            timer: 1500
          }
          )
        }
        
      });
  });

  
  $(document).ready(function() {
    $('#farmerItemSwitchCheck').change(function() {
      if ($(this).prop('checked')) {
        $('#switchLabel').text('เปิดการใช้งาน');
      } else {
        $('#switchLabel').text('ปิดการใช้งาน');
      }
    });
  });