$(document).ready(function() {
    console.log("Initializing Select2...");  // Debugging: Log initialization
    $('.select2-enable').select2({
        tags: true,  // Allow free typing
        placeholder: "Search or create an event...",
        allowClear: true,
        ajax: {
            url: "/bills/event-autocomplete/",
            dataType: 'json',
            delay: 250,
            data: function (params) {
                console.log("Sending AJAX request with term:", params.term);  // Debugging: Log search term
                return {
                    q: params.term,  // Search term
                };
            },  
            processResults: function (data) {
                console.log("Response data:", data);  // Debugging: Log the response
                return { 
                    results: data.results,
                    pagination: {
                        more: data.pagination.more  
                    } 
                };
            }
        },
        createTag: function (params) {
            var term = $.trim(params.term);
            return term ? { id: term, text: term, newTag: true } : null;
        }
    });
});

