(require 'org)
(require 'ox)
(require 'ox-html)

(org-export-define-derived-backend 'pelican-html 'html
  :translate-alist '((src-block .  pygments-org-html-code)
                     (example-block . pygments-org-html-code)))

(defvar pygments-path "pygmentize")

(defun pygments-org-html-code (code contents info)
  "Process code block with Pygments
See http://pygments.org/ for details"

  ;; Generate temp file path by hashing current time and date.
  (setq temp-source-file(format "/tmp/pygmentize-%s.txt"(md5 (current-time-string))))
  ;; Writing temp file
  (with-temp-file temp-source-file (insert (org-element-property :value code)))
  ;; Processing
  (shell-command-to-string (format "%s -l \"%s\" -f html %s"
                                   pygments-path
                                   (org-element-property :language code)
                                   temp-source-file)))

(provide 'pelican-html)
