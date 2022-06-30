function ajaxSend(url,params){

    fetch(`${url}?${params}`,{
        method: 'GET',
        headers: {
            'Content-Type' : 'application/x-www-form-urlencoded',
            },
        })
            .then(response => response.json())
            .then(json => render(json))
            .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit',function (e){
   e.preventDefault();
   let url = this.action;
   let params = new URLSearchParams(new FormData(this)).toString();
   ajaxSend(url, params)
});

function render(data){
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.left-ads-display>.row');
    div.innerHTML = output
}
let html = '\
{{ #models }}\
    <div class="main-block">\
        <div class="content">\
            <img src="media/{{ poster }}" alt="cover" class="content_image" height="150px" style="padding-left: 30px">\
            <div class="content_info">\
                <div class="flex">\
                    <p class="content_category">{{ title }}</p>\
                    <p class="price">{{ price }}$</p>\
                </div>\
                <div class="too"><a href="/{{ url }}" class="cotent_button">подробнее</a></div>\
            </div>\
        </div>\
    </div>\
{{ /models }}'



