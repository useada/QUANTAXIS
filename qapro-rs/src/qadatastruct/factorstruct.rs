use polars::prelude::{CsvReader, DataFrame, DataType, Field, NamedFrom, ParquetReader, Schema, SerReader, Series, SortMultipleOptions};

fn QADataStruct_Factor_schema() -> Schema {
    Schema::new(
    // vec![
    //     Field::new("date", DataType::Utf8),
    //     Field::new("order_book_id", DataType::Utf8),
    //     Field::new("factor", DataType::Float32),
    // ]
    )
}

// same with python model :: // qafactor Daily struct
pub struct QADataStruct_Factor {
    pub data: DataFrame,
    name: String,
}

impl QADataStruct_Factor {
    pub fn new_from_vec(
        date: Vec<String>,
        order_book_id: Vec<String>,
        factor: Vec<f32>,
        factorname: String,
    ) -> Self {
        let dateS = Series::new("date", &date);

        let order_book_idS = Series::new("order_book_id", &order_book_id);
        let factorS = Series::new("factor", &factor);
        let df = DataFrame::new(vec![dateS, order_book_idS, factorS]).unwrap();
        Self {
            data: df
                .sort(&["date", "order_book_id"], SortMultipleOptions::default().with_order_descending_multi(&[false, false]))
                .unwrap(),
            name: factorname,
        }
    }
}
