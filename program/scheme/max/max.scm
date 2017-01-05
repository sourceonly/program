; use prefix p- to avoid overiden of the default max                                        ;
(define (p-max p-list)
  (cond ((null? p-list) '())
        ((null? (cdr p-list)) (car p-list))
        (else (max (car p-list) (p-max (cdr p-list))))
        ))

(define (p-min p-list)
  (define (opposite-list x    )
    (* -1 x))
  (opposite-list (p-max (map opposite-list p-list))))
