git clone git://github.com/ruby-numo/narray; git clone git://github.com/ruby-numo/linalg; 
gem update --no-document --system
gem install --no-document bundler daru iruby nyaplot pry rbczmq
cd narray
gem build numo-narray.gemspec
gem install numo-narray-0.9.0.2.gem
cd ../linalg
rake build
gem install pkg/numo-linalg-0.0.1.gem -- --with-openblas
iruby register
