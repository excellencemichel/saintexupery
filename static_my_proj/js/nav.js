	// var menuItems = document.querySelectorAll('.ui__menu__item.has__child') ;

	// menuItems.forEach(function (item , id) {
	// 	item.addEventListener('click' ,function (e) {
	// 		var _this = e.target ;
	// 		//
	// 		var currentActiveItem = document.querySelector('.ui__menu__item.has__child.ui__menu__active__item')
	// 		if (currentActiveItem) {
	// 			currentActiveItem.classList.remove('ui__menu__active__item') ;
	// 		}
	// 		_this.classList.toggle('ui__menu__active__item') ;
	// 	})
	// })
	var menuShower = document.querySelector('#menu__shower') ;
	var menuListContainer = document.querySelector('.ui__menu__list') ;
	menuShower.addEventListener('click' , function (e) {
		e.preventDefault() ;
		menuListContainer.classList.toggle('show__menu__list') ;

	})

	var header = document.querySelector('.ui__header')

	window.addEventListener('scroll' , function () {
		var headerHeight = header.getBoundingClientRect().height ;
		var scrollY = window.scrollY ;
		console.log(headerHeight , scrollY) ;
		if (scrollY > headerHeight) {
			if (header.classList.contains('ui__fix__header')) { return ; }
			header.classList.add('ui__fix__header') ;
		}else {
			if (!header.classList.contains('ui__fix__header')) { return ; }
			header.classList.remove('ui__fix__header') 
		}
	})