let erode = $('#erode');
let kernel_erode = $('#kernel_erode');
let range_erode = $('#range_erode');

let dilate = $('#dilate');
let kernel_dilate = $('#kernel_dilate');
let range_dilate = $('#range_dilate');

let threshold = $('#threshold');
let type_threshold = $('#type_threshold');
let max_threshold = $('#max_threshold');
let range_threshold = $('#range_threshold');

let row_filter = $('.row-filter');

let aplicar_config = $('#aplicar_config');

$(document).ready(function(){
  row_filter.each(function(){
    if($(this).find('input[type="checkbox"]').prop('checked') == false){
      $(this).children().find('select').attr('disabled', 'disabled');
      $(this).children().find('input[type="range"]').attr('disabled', 'disabled');
      $(this).children().find('input[type="number"]').attr('disabled', 'disabled');
    }
  });
});

erode.on('change', function(){
  if($(this).prop('checked') == true){
    kernel_erode.removeAttr('disabled');
    range_erode.removeAttr('disabled');
  } else{
    kernel_erode.attr('disabled', 'disabled').val('0');
    range_erode.attr('disabled', 'disabled');
  }
});

dilate.on('change', function(){
 if($(this).prop('checked') == true){
    kernel_dilate.removeAttr('disabled');
    range_dilate.removeAttr('disabled');
  } else{
    kernel_dilate.attr('disabled', 'disabled').val('0');
    range_dilate.attr('disabled', 'disabled');
  }
});

threshold.on('change', function(){
  if($(this).prop('checked') == true){
    type_threshold.removeAttr('disabled');
    range_threshold.removeAttr('disabled');
    if(type_threshold.val() == 0 || type_threshold.val() == 1){
      max_threshold.removeClass('hidden').removeAttr('disabled');
    } else{
      max_threshold.addClass('hidden').attr('disabled', 'disabled');
    }
  } else{
    type_threshold.attr('disabled', 'disabled').val('0');
    range_threshold.attr('disabled', 'disabled');
    max_threshold.addClass('hidden').attr('disabled', 'disabled');
  }
});

type_threshold.on('change', function(){
  if(type_threshold.val() == 0 || type_threshold.val() == 1){
    max_threshold.removeClass('hidden').removeAttr('disabled');
  } else{
    max_threshold.addClass('hidden').attr('disabled', 'disabled');
  }
});

// aplicar_config.on('click', function(e){
//   e.preventDefault();
//   let form = $('#form_configuracao');
//   visualizar(form);
// });

// function visualizar(form){
//   let imagem = $('#processed_image');
//   $.ajax({
//     url: "/visualizar",
//     method: 'post',
//     data: form.serialize(),
//     datatype: 'json',
//     success: function(data){
//       imagem.append(data);
//       // let response = JSON.parse(data);
//       // imagem.append('<img>');
//     }
//   });
// }