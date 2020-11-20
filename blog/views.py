from django.shortcuts import render

posts = [{
    "author": "Royal McMylor",
    "title": "Ratufa indica",
    "content": "In sagittis dui vel nisl. Duis ac nibh. Fusce lacus purus, aliquet at, feugiat non, pretium quis, lectus. Suspendisse potenti. In eleifend quam a odio. In hac habitasse platea dictumst. Maecenas ut massa quis augue luctus tincidunt. Nulla mollis molestie lorem. Quisque ut erat.",
    "date_posted": "3/24/2020"
}, {
    "author": "Freda Ferney",
    "title": "Streptopelia senegalensis",
    "content": "Nulla mollis molestie lorem. Quisque ut erat. Curabitur gravida nisi at nibh. In hac habitasse platea dictumst. Aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. Integer tincidunt ante vel ipsum. Praesent blandit lacinia erat. Vestibulum sed magna at nunc commodo placerat. Praesent blandit. Nam nulla.",
    "date_posted": "2/7/2020"
}, {
    "author": "Farah Scotti",
    "title": "Odocoileus hemionus",
    "content": "Vivamus tortor. Duis mattis egestas metus. Aenean fermentum. Donec ut mauris eget massa tempor convallis. Nulla neque libero, convallis eget, eleifend luctus, ultricies eu, nibh. Quisque id justo sit amet sapien dignissim vestibulum.",
    "date_posted": "5/16/2020"
}, {
    "author": "Weylin Ottosen",
    "title": "Vombatus ursinus",
    "content": "Donec quis orci eget orci vehicula condimentum.",
    "date_posted": "1/23/2020"
}, {
    "author": "Zulema Deery",
    "title": "Uraeginthus granatina",
    "content": "Etiam vel augue. Vestibulum rutrum rutrum neque. Aenean auctor gravida sem. Praesent id massa id nisl venenatis lacinia. Aenean sit amet justo. Morbi ut odio. Cras mi pede, malesuada in, imperdiet et, commodo vulputate, justo. In blandit ultrices enim. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Proin interdum mauris non ligula pellentesque ultrices.",
    "date_posted": "2/5/2020"
}, {
    "author": "Glyn Rawdall",
    "title": "Galictis vittata",
    "content": "Integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. Mauris lacinia sapien quis libero. Nullam sit amet turpis elementum ligula vehicula consequat. Morbi a ipsum. Integer a nibh. In quis justo. Maecenas rhoncus aliquam lacus.",
    "date_posted": "6/25/2020"
}, {
    "author": "Weidar Cornbell",
    "title": "Macaca radiata",
    "content": "Praesent lectus. Vestibulum quam sapien, varius ut, blandit non, interdum in, ante. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Duis faucibus accumsan odio. Curabitur convallis. Duis consequat dui nec nisi volutpat eleifend.",
    "date_posted": "12/29/2019"
}, {
    "author": "Doralyn Emlyn",
    "title": "Cebus nigrivittatus",
    "content": "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est. Donec odio justo, sollicitudin ut, suscipit a, feugiat et, eros. Vestibulum ac est lacinia nisi venenatis tristique.",
    "date_posted": "1/7/2020"
}, ]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context, )


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
