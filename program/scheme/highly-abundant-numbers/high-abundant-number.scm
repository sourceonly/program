#!/usr/bin/guile -s
!#
(define (find-divisor p)
  (define (find-divisor-iter p current divisor-list)
    (cond ((eq? current 0) divisor-list)
          ((eq? (remainder p current) 0) (find-divisor-iter p (- current 1) (cons current divisor-list)))
          (else (find-divisor-iter p (- current 1) divisor-list))))
  (find-divisor-iter p p '()))


(define (print-abundant current current-max)
  (let ((d-list (find-divisor current)))
    (let ((s (apply + d-list)))
      (cond ((> s current-max) 
             (begin (display current)
                    (display "-----")
                    (display current-max)
                    (newline)
                    (print-abundant (+ 1 current) s)))
            (else (print-abundant (+ 1 current) current-max))))))

(print-abundant 1 0)
