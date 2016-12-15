#!/usr/bin/guile -s
!#

(define (reverse-list p-list )
  "reverse the given list, of course O(n), where n is the length of list"
  (define (reverse-iter p-list q-list)
    (if (null? p-list)
	q-list
	(reverse-iter (cdr p-list ) (cons (car p-list) q-list))))
  (reverse-iter p-list '()))

(define (get-list-length p-list)
  "iteration through all list members, get it's length,  O(n)"
  (if (null? p-list)
      0
      (+ 1 (get-list-length (cdr p-list)))))
(define (kth-swap p-list k)
  (define length-of-list (get-list-length p-list))
  (define reverse-p-list (reverse-list p-list))
  (define (kth-iter p-list q-list j k r-list)
    (cond ((null? p-list) r-list)
	  ((= k 0) (kth-iter (cdr p-list) (cdr q-list) (- j 1) (- k 1) (cons (car p-list) r-list)))
	  ((= j 0) (kth-iter (cdr p-list) (cdr q-list) (- j 1) (- k 1) (cons (car p-list) r-list)))
	  (else (kth-iter  (cdr p-list) (cdr q-list) (- j 1) (- k 1) (cons (car q-list) r-list)))))
  (kth-iter p-list reverse-p-list (- k 1) (- length-of-list k) '()))



(display (kth-swap '(a b c d e) 5))

