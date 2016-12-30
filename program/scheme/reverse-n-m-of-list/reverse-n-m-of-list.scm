(define (append-nth elem m p-list)
  (cond ((= m 0) (cons elem p-list))
        ((null? p-list) (cons elem p-list))
        (else (cons (car p-list) (append-nth elem (- m 1) (cdr p-list)))))
  )

(define (rev-n-m n m p-list)
  (cond ((> n m) (rev-n-m m n p-list))
        ((= m 0) p-list)
        ((null? p-list) p-list)
        ((> n 0) (cons (car p-list) (rev-n-m (- n 1) (- m 1) (cdr p-list))))
        ((= n 0) (append-nth (car p-list) m (rev-n-m n (- m 1) (cdr p-list))))

        )

  )
(define a (rev-n-m 1 3 '( a b c d e f)))
