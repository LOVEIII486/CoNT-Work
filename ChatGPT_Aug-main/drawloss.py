import matplotlib.pyplot as plt
import os

imgPath = 'loss/img'
nll_loss = []
cl_loss = []
all_loss = []
nll_loss_smp = []
cl_loss_smp = []
all_loss_smp = []
nll_loss_stp = []
cl_loss_stp = []
all_loss_stp = []
nll_loss_txt = open('loss/nll_loss.txt')
cl_loss_txt = open('loss/cl_loss.txt')

for line in nll_loss_txt:
    nll_loss.append(line.strip("\n"))
for line in cl_loss_txt:
    cl_loss.append(line.strip("\n"))

for item in range(0, len(nll_loss) - 1, 100):
    nll_loss_smp.append(float(nll_loss[item]))
    nll_loss_stp.append(item)
for item in range(0, len(cl_loss) - 1, 200):
    cl_loss_smp.append(float(cl_loss[item]))
    cl_loss_stp.append(item)
# print('Epoch {}, loss {:.4f}'.format(epoch, epoch_loss))
# epoch_losses.append(epoch_loss)


# plt.plot(nll_loss_stp,nll_loss_smp,'g-',label=u'Dense_Unet(block layer=5)')
# ‘’g‘’代表“green”,表示画出的曲线是绿色，“-”代表画的曲线是实线，可自行选择，label代表的是图例的名称，一般要在名称前面加一个u，如果名称是中文，会显示不出来，目前还不知道怎么解决。
plt.figure(1)
p1 = plt.plot(nll_loss_stp, nll_loss_smp, 'b-', label=u'nll_loss')
plt.legend()
plt.xlabel(u'iters')
plt.ylabel(u'loss')
plt.title('loss for nll in training')
plt.savefig(os.path.join(imgPath, "nll_loss.png"))

plt.figure(2)
p2 = plt.plot(cl_loss_stp, cl_loss_smp, 'g-', label=u'cl_loss')
plt.legend()
plt.xlabel(u'iters')
plt.ylabel(u'loss')
plt.title('loss for contrastive learning in training')
plt.savefig(os.path.join(imgPath, "cl_loss.png"))
