source /usr/local/share/chruby/chruby.fish
source /usr/local/share/chruby/auto.fish
starship init fish | source
direnv hook fish | source

alias g=git
alias be="bundle exec"

function aws
  command aws2 $argv
end


# Rails aliases
# alias rc='rails console'
# alias rcs='rails console --sandbox'
# alias rd='rails destroy'
# alias rdb='rails dbconsole'
# alias rgen='rails generate'
# alias rgm='rails generate migration'
# alias rp='rails plugin'
# alias ru='rails runner'
# alias rs='rails server'
# alias rsd='rails server --debugger'
# alias rsp='rails server --port'

# Rake aliases
# alias rdm='rake db:migrate'
# alias rdms='rake db:migrate:status'
# alias rdr='rake db:rollback'
# alias rdc='rake db:create'
# alias rds='rake db:seed'
# alias rdd='rake db:drop'
# alias rdrs='rake db:reset'
# alias rdtc='rake db:test:clone'
# alias rdtp='rake db:test:prepare'
# alias rdmtc='rake db:migrate db:test:clone'
# alias rdsl='rake db:schema:load'
# alias rlc='rake log:clear'
# alias rn='rake notes'
# alias rr='rake routes'
# alias rrg='rake routes | grep'
# alias rt='rake test'
# alias rmd='rake middleware'
# alias rsts='rake stats'
