$(function () {

    $("#all_types").click(function () {

        console.log("全部类型");

        $("#all_types_container").show();

        var all_type = $(this);

        all_type.find("span").find("span").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");

        $("#sort_rule_container").slideUp();

        $("#sort_rule span span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    })


    $("#all_types_container").click(function () {

        var all_types_container = $(this);

        all_types_container.hide();

        var all_type = $("#all_types");

        all_type.find("span").find("span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");


    })


    $("#sort_rule").click(function () {

        $("#sort_rule_container").slideDown();

        var sort_rule = $(this);

        sort_rule.find("span").find("span").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");

        $("#all_types_container").hide();

        $("#all_types span span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    })

    $("#sort_rule_container").click(function () {

        var sort_rule_container = $(this);

        sort_rule_container.slideUp();

        var sort_rule = $("#sort_rule");

        sort_rule.find("span").find("span").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");


    })


    $(".addShopping").click(function () {

        console.log("添加到购物车");

        var btn = $(this);

        // console.log(btn.attr("class"));
        //
        // console.log(btn.prop("class"));
        //
        // console.log(btn.attr("goodsid"));
        //
        // console.log(btn.prop("goodsid"));

        var goodsid = btn.attr("goodsid");

        //   /axf/addtocart/?goodsid=value

        $.getJSON("/axf/addtocart/",{"goodsid": goodsid},function (data) {
            console.log(data);

            window.open("/axf/home/", target="_self");
        })

    })

})