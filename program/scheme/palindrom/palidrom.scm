(define (palindrom-list? p-list)
  (cond ((null? p-list) #t)
        ((null? (cdr p-list)) #t)
        (else (let ((t (tcdr p-list)))
                (and (palindrom? (tcar (cdr p-list))) (eq? (car p-list) t)))
        )

  ))



(define (tcar p-list)
  (cond ((null? p-list) p-list         )
        ((null? (cdr p-list)) '())
        (else (cons (car p-list) (tcar (cdr p-list)))))

  )

(define (tcdr p-list)
  (cond ((null? p-list) p-list         )
        ((null? (cdr p-list)) (car p-list))
        (else (tcdr (cdr p-list)))))
