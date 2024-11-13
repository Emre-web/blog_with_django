from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from .models import Post,Comment
from .forms import CommentForm,PostForm

def home(request):
    posts = Post.objects.all()
    return render(request,'blog/home.html',{'posts':posts})


def post_detail(request, id):
    post = get_list_or_404(Post,id=id)
    comments = Comment.objects.all()#bu iki satırırn anlamı şudur: post id'si ile eşleşen postu alır ve eğer post yoksa 404 hatası döndürür.
    if request.method == 'POST':
        comment_form = CommentForm(request.POST) #bu kod şu işe yaraR: kullanıcı formu doldurduktan sonra formu gönderdiğinde, formu alıp işlem yapmamızı sağlar.
        if comment_form.is_valid(): #eğer bu kosul sağlanıyorsa, yani form doğruysa, aşağıdaki kodları çalıştırır.
            new_comment = comment_form.save(commit=False) #burada commit=False dememizin sebebi, formu kaydetmek istediğimizi belirtmek. Eğer commit=False demezsek, formu kaydeder ve bize geri döndürür. Biz ise formu kaydetmek istemediğimizi belirttik.   
            #neden false yaptık ama ? çünkü biz formu kaydetmek istemiyoruz. Çünkü biz formu kaydettikten sonra, formun postu olmadığını gördük. Bu yüzden formu kaydetmek istemiyoruz.
            new_comment.post = post #yeni yorumun postu, post olacak.
            new_comment.save()          
            return redirect('post_detail', id.post.id) #yorumu kaydettikten sonra, yorumun postunun detay sayfasına geri dönmek istiyoruz.

#eğer bir post olusturmuyor ve commit etmiyorsak sunu yapalım:
        else:
            comment_form = CommentForm()
        return render(request,'blog/post_detail.html',{
            'post':post,
            'comments':comments,
            'comment_form':comment_form
        }),
        #bu satırlarda, postun detay sayfasına yorum eklemek için gerekli olan kodları yazdık. Şimdi bu kodları post_detail.html dosyasında kullanacağız.


        #bir post olusturma işlemi
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')

    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html',{'form':form}) #bu kodlar, yeni bir post oluşturmak için gerekli olan kodlardır. Şimdi bu kodları post_edit.html dosyasında kullanacağız. 

#bir postu düzenleme işlemi
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)   
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)


#tersi bi durumda, yani post düzenleme işlemi yapmıyorsak, yani sadece postu göstermek istiyorsak:
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
#bu kodlar, postu düzenlemek için gerekli olan kodlardır. Şimdi bu kodları post_edit.html dosyasında kullanacağız.


def post_delete(request, id):
    post = get_object_or_404(Post, id=id) #get_object_or_404 fonksiyonu, postun id'si ile eşleşen postu alır ve eğer post yoksa 404 hatası döndürür.
    post.delete()
    return redirect('home')