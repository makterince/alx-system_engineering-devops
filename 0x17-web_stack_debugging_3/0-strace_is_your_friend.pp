# Install required packages or dependencies
exec {'searchAndReplace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
