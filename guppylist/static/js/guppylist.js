$(function () {
    $.ajaxSettings.traditional = true;
    $("[data-toggle='popover']").popover();

    $('#search-field').typeahead({
        name: 'products',
        local: ['hello', 'world'],
        limit: 10,
    });

    // $('#search-field').typeahead({
    //     name: 'products',
    //     remote: {
    //         url: 'http://completion.amazon.com/search/complete?q=%QUERY&search-alias=videogames&mkt=1',
    //         dataType: 'jsonp',
    //     },
    //     remote: 'http://completion.amazon.com/search/complete?method=completion&q=kindle&search-alias=videogames&mkt=1',
    //     local: ['hello', 'world'],
    //     limit: 10,
    // });
    /*
    $('#search-field').typeahead({
        minLength: 2,
        items: 30,
        source: function(q, process) {
            var data = new Array;

            return $.ajax({
                url: 'http://completion.amazon.com/search/complete',
                type: 'GET',
                cache: false,
                dataType: 'jsonp',
                success: function (response) {
                    for (var i in response[1]) {
                        data.push(response[1][i]);
                    }
                    return process(data);
                },
                data: {
                    q: q,
                    'search-alias': 'videogames',
                    mkt: '1',
                    callback: '?'
                }
            });
        },
        updater: function(item) {
            this.$element[0].value = item;
            this.$element[0].form.submit();
            return item;
        }
    });
    */
});