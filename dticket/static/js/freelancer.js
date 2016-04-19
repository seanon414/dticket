//Pause makes counter blink, Resume to remove
(function ($) {
    "use strict";

    /*global window */

    var dt_ticket = {
        init: function () {
            var self = this;
            this.pause_counter();
            this.resume_counter();
            this.set_counter();

            $("[name='button_next']").on("click", function (e) {
                e.preventDefault();
                self.increment_counter();
                self.set_counter();
                $(this).closest("form").submit();
            });

            $("[name='button_back']").on("click", function (e) {
                e.preventDefault();
                self.decrement_counter();
                self.set_counter();
                $(this).closest("form").submit();
            });
        },

        set_counter: function () {
            $(".serve_number").text($("#id_ticket_number").val());
        },

        pause_counter: function () {
            var self = this;
            $("[name='button_pause']").on("click", function () {
                $(".serve_number").addClass("blink");
                setInterval(function () {
                    $(".blink").fadeOut(500);
                    $(".blink").fadeIn(500);
                }, 1000);
                $(this).text("Resume");
                $(this).attr("name", "button_resume");
                self.resume_counter();
            });
        },

        resume_counter: function () {
            var self = this;
            $("[name='button_resume']").on("click", function () {
                $(".serve_number").removeClass("blink");
                $(this).text("Pause");
                $(this).attr("name", "button_pause");
                self.pause_counter();
            });
        },

// Next increments counter
        increment_counter: function () {
            var counter = $("#id_ticket_number").val();
            counter ++;
            $("#id_ticket_number").val(counter.toString());
        },

        decrement_counter: function () {
            var counter = $("#id_ticket_number").val();
            counter --;
            $("#id_ticket_number").val(counter.toString());
        }

    };

    dt_ticket.init();
}(window.jQuery));

/*!
 * Start Bootstrap - Freelancer Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('body').on('click', '.page-scroll a', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Floating label headings for the contact form
$(function() {
    $("body").on("input propertychange", ".floating-label-form-group", function(e) {
        $(this).toggleClass("floating-label-form-group-with-value", !! $(e.target).val());
    }).on("focus", ".floating-label-form-group", function() {
        $(this).addClass("floating-label-form-group-with-focus");
    }).on("blur", ".floating-label-form-group", function() {
        $(this).removeClass("floating-label-form-group-with-focus");
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
    $('.navbar-toggle:visible').click();
});
