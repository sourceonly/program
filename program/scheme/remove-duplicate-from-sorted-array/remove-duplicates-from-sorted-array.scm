(define (append-list elem p-list)
  (if (null? p-list )
      (cons elem p-list)
      (cons (car p-list) (append-list elem (cdr p-list))))
  )

(define (reverse-list p-list)
  (if (null? p-list)
      p-list
      (append-list (car p-list) (cdr p-list))
      )
  )



(define (append-nth elem p-list n)
  (if (= n 0)
      (cons elem p-list)
      (cons (car p-list) (append-nth elem (cdr p-list) (- n 1)))
      )
  )

(define (reverse-n-m p-list n m)
  (cond ((> n m) (reverse-n-m p-list m n))
        ((= n 0) (cons (car p-list) (reverse-n-m (cdr p-list) n (- m 1))))
        ((> n 0) (cons (car p-list) (reverse-n-m (cdr p-list) (- n 1) (- m 1))))
        ((> m 0) (append-nth (car p-list) (reverse-n-m p-list n m )))
        ((= m 0) p-list)
        ))
