- add english country name column
  ```shell
  python map_en_country.py
  ```
  this will use `country_mapping.json` to generate `new.ip.merge.txt`

- make database
  ```shell
  ${ip2region_root}/maker/cpp/xdb_make --db ${ip2region_root}/data/ip2region_yh.xdb --src ${ip2region_root}/data/new.ipv4_source.txt
  ```

- rebuild dev image for new ip2region database