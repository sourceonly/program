(define (walk-list? p-list max-num)
;  (display max-num)
  (cond ((null? p-list) #t)
        ((not (> max-num 0)) #f)
        (else (walk-list? (cdr p-list) (max (car p-list) (- max-num 1))))
        )

  )

(define (list-can-walk? p-list)
  (walk-list? p-list (car p-list))
  )


(display (list-can-walk? '(5 4 3 2 1 0 1 2 3 4 5  )))
