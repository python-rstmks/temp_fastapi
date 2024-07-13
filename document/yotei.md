すべてのクエスチョン数をカウントして　 

　 

 

それをファイルエクスポートと一緒にだす。 

 

エクスポートで出力されるフォルダに入っているファイルは以下の構成。計6つのファイル 

 

Category 一覧（csv) 

 

Subcategory一覧(csv) 

 

Question一覧 

 

Subcategory-quetion　テーブル　の一覧 

 

マスタデータ（カテゴリ数、subcategory数、question数） 

 

＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝ 

 

もしくは　エクスポート処理、インポート処理を　カテゴリ単位で行う。 

カテゴリ一覧ファイルも一緒に渡すことで、例えばmathファイルをインポートするのを忘れていたときに、フロントエンドに　mathファイルが読み込まれていません。とアラートを出す機能を作成することができる。 

 

Ex) economics 

 

インポートのロジックで　例えば　economicsのカテゴリを作成したら　 

new_question = Question(**question_data) 

db.add(new_question) 

db.commit() 

 
 

new_category_question = CategoryQuestion(category_id=question_create.category_id, question_id=new_question.id) 

new_subcategory_question = SubCategoryQuestion(subcategory_id=question_create.subcategory_id, question_id=new_question.id) 

 

上記のように　そのカテゴリid を取得して　そこからsubcategoryを作成する 

 

さらにそのsubcateogry_idを取得して　そこからquetionを作成する 

 

 

``` 

{ 

  "category": "chemistry", 

  "subcategories": [ 

    { 

      "subcategory": "organic-chemistry", 

      "questions": [ 

        { 

          "problem": "構造決定とは？", 

          "answer": "手法です", 

          "is_correct": true 

        }, 

        { 

          "problem": "有機化合物とは？", 

          "answer": "炭素を含む化合物です", 

          "is_correct": true 

        } 

      ] 

    }, 

    { 

      "subcategory": "inorganic-chemistry", 

      "questions": [ 

        { 

          "problem": "硫黄とは？", 

          "answer": "物質です。", 

          "is_correct": true 

        }, 

        { 

          "problem": "無機化合物とは？", 

          "answer": "炭素を含まない化合物です", 

          "is_correct": true 

        } 

      ] 

    }, 

    { 

      "subcategory": "theoretical-chemistry", 

      "questions": [ 

        { 

          "problem": "蒸発とは？", 

          "answer": "現象です", 

          "is_correct": true 

        }, 

        { 

          "problem": "理論化学とは？", 

          "answer": "化学の理論的な研究です", 

          "is_correct": true 

        } 

      ] 

    } 

  ] 

} 

 

 

``` 

 

 

こんな感じで作成するか 

 

↓gptに作成させたimportのおおまかなロジック 

 

from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Table 

from sqlalchemy.orm import relationship, sessionmaker, declarative_base 

  

Base = declarative_base() 

  

# Association table for many-to-many relationship 

subcategory_question_association = Table( 

    'subcategory_question', Base.metadata, 

    Column('subcategory_id', Integer, ForeignKey('subcategories.id')), 

    Column('question_id', Integer, ForeignKey('questions.id')) 

) 

  

class Category(Base): 

    __tablename__ = 'categories' 

    id = Column(Integer, primary_key=True) 

    name = Column(String, unique=True) 

  

class Subcategory(Base): 

    __tablename__ = 'subcategories' 

    id = Column(Integer, primary_key=True) 

    name = Column(String) 

    category_id = Column(Integer, ForeignKey('categories.id')) 

    category = relationship("Category", back_populates="subcategories") 

    questions = relationship( 

        "Question", 

        secondary=subcategory_question_association, 

        back_populates="subcategories" 

    ) 

  

class Question(Base): 

    __tablename__ = 'questions' 

    id = Column(Integer, primary_key=True) 

    problem = Column(String) 

    answer = Column(String) 

    is_correct = Column(Boolean) 

    subcategories = relationship( 

        "Subcategory", 

        secondary=subcategory_question_association, 

        back_populates="questions" 

    ) 

  

Category.subcategories = relationship("Subcategory", order_by=Subcategory.id, back_populates="category") 

  

# Database setup 

engine = create_engine('sqlite:///chemistry.db') 

Base.metadata.create_all(engine) 

  

Session = sessionmaker(bind=engine) 

session = Session() 

  

# JSON data 

import json 

  

json_data = ''' 

{ 

  "category": "chemistry", 

  "subcategories": [ 

    { 

      "subcategory": "organic-chemistry", 

      "questions": [ 

        { 

          "problem": "構造決定とは？", 

          "answer": "手法です", 

          "is_correct": true 

        }, 

        { 

          "problem": "有機化合物とは？", 

          "answer": "炭素を含む化合物です", 

          "is_correct": true 

        } 

      ] 

    }, 

    { 

      "subcategory": "inorganic-chemistry", 

      "questions": [ 

        { 

          "problem": "硫黄とは？", 

          "answer": "物質です。", 

          "is_correct": true 

        }, 

        { 

          "problem": "無機化合物とは？", 

          "answer": "炭素を含まない化合物です", 

          "is_correct": true 

        } 

      ] 

    }, 

    { 

      "subcategory": "theoretical-chemistry", 

      "questions": [ 

        { 

          "problem": "蒸発とは？", 

          "answer": "現象です", 

          "is_correct": true 

        }, 

        { 

          "problem": "理論化学とは？", 

          "answer": "化学の理論的な研究です", 

          "is_correct": true 

        } 

      ] 

    } 

  ] 

} 

''' 

  

data = json.loads(json_data) 

  

# Insert data into the database 

category = Category(name=data['category']) 

session.add(category) 

session.commit() 

  

for subcat_data in data['subcategories']: 

    subcategory = Subcategory(name=subcat_data['subcategory'], category=category) 

    session.add(subcategory) 

    session.commit() 

  

    for question_data in subcat_data['questions']: 

        question = Question( 

            problem=question_data['problem'], 

            answer=question_data['answer'], 

            is_correct=question_data['is_correct'] 

        ) 

        subcategory.questions.append(question) 

        session.add(question) 

    session.commit() 

  

# Verify the data 

for cat in session.query(Category).all(): 

    print(f"Category: {cat.name}") 

    for subcat in cat.subcategories: 

        print(f"  Subcategory: {subcat.name}") 

        for question in subcat.questions: 

            print(f"    Question: {question.problem}") 

            print(f"    Answer: {question.answer}") 

            print(f"    Is Correct: {question.is_correct}") 

 

 

=============== 

Exportロジック 

 

def export_data(): 

    categories = session.query(Category).all() 

    export_dict = {"categories": []} 

  

    for category in categories: 

        category_dict = {"name": category.name, "subcategories": []} 

        for subcategory in category.subcategories: 

            subcategory_dict = {"name": subcategory.name, "questions": []} 

            for question in subcategory.questions: 

                question_dict = { 

                    "problem": question.problem, 

                    "answer": question.answer, 

                    "is_correct": question.is_correct 

                } 

                subcategory_dict["questions"].append(question_dict) 

            category_dict["subcategories"].append(subcategory_dict) 

        export_dict["categories"].append(category_dict) 

  

    with open('exported_data.json', 'w', encoding='utf-8') as f: 

        json.dump(export_dict, f, ensure_ascii=False, indent=4) 

  

# データのエクスポート 

export_data() 

 

 

 