- add english country name column
  ```shell
  python map_en_country.py
  ```
  this will use `country_mapping.json` to generate `new.ip.merge.txt`

- make database
  ```shell
  java -jar ${ip2region_root}/maker/java/dbMaker-1.2.2.jar -src new.ip.merge.txt -region global_region.csv -dst ${ip2region_root}
  ```

- rebuild dev image for new ip2region database