#!/usr/bin/guile -s
!#

(define (get-most-time-cons p-list)
  (define (get-most-time-cons-iter cme cmc ce cc p-list)
    (cond ((> cc cmc) (get-most-time-cons-iter ce cc ce cc p-list))
	  ((null? p-list)
	   (begin (display cmc) (display " ")
	   cme))
	  (else
	   (if (eq? (car p-list) ce)
	       (get-most-time-cons-iter cme cmc ce (+ cc 1) (cdr p-list))
	       (get-most-time-cons-iter cme cmc (car p-list) 1 (cdr p-list))))))
  (get-most-time-cons-iter (car p-list) 0 (car p-list) 0 p-list))

(newline)
(display (get-most-time-cons '(a a a a a a a a b b b b b b b b b c d d e e e e f f f f f f f f f f f )))
(newline)
