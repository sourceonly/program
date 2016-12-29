(define (add-to-first p-list)
  (cond ((null? (cdr p-list)) p-list)
        (else (cons (+ (car p-list) (car (cdr p-list))) (add-to-first (cdr p-list))))
        )
  )

(define (pas-t p-list)
  (let ((s (cons (car p-list) (add-to-first p-list))))
    (display s)
    (newline)
    (pas-t s))
  )

(pas-t '(1))
