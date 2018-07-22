$(function () {
    /**
     * $(fun)   准备好
     *          加载好
     *    准备好是指页面的html的基本结构加载完成
     *
     *    加载好是指页面中的所有内容都加在好
     *
     *    准备好优于加载好 进行执行
     */
    initeTopSwiper();
    initSwiperMenu();

})

function initeTopSwiper() {

    var swiper = new Swiper("#topSwiper", {
        loop: true,
        autoplay: 3000,
        pagination: ".swiper-pagination"
    });

}


function initSwiperMenu() {

    var swiper = new Swiper("#swiperMenu",{
        slidesPerView: 3
    })

}