(define (insert-elem elem p-list op)
  (cond ((null? p-list) (cons elem p-list))
        ((not (op elem (car p-list))) (cons (car p-list) (insert-elem elem (cdr p-list) op)))
        (else (cons elem p-list))
      )
  )

(define (sort-list p-list op)
  (if (null? p-list)
      p-list
      (insert-elem (car p-list) (sort-list (cdr p-list) op) op
      )
  ))
