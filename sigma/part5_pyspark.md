# Write a query to display all rows where the `publish_date` is greater than 2022-01-1.
```python
df.filter(df.metadata.publish_date > lit("2022-01-01"))
```

# Add an new column which, for each row, is an array of all of the `text` elements within `ner_results`.
```python
df.withColumn("new_col", split(df.ner_results.element.text, " "))
```

# Write a query to display all of the unique values for `code` in the `region` column.
```python
df.select("region.code").distinct().show()
```